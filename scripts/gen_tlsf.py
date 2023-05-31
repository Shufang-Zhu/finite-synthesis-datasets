# -*- coding: utf-8 -*-
import os
import subprocess
from pathlib import Path
from typing import Dict, List, Optional

import click



# @click.command()
# @click.option("--dataset", default=None)
# @click.option("--save", default=None, type=click.Path(dir_okay=True, writable=True))

def transform(dataset, save):
    dataset_path = Path("../Spot-format/"+dataset)
    tlsf_path = Path(str(save)) / Path(dataset)
    tlsf_path.mkdir(parents=True, exist_ok=True)
    for file in sorted(dataset_path.glob("./*.ltlf")):
        tlsf_file = tlsf_path / f"{file.stem}.tlsf"
        tlsf = transform_tlsf(dataset, file)

        Path(tlsf_file).write_text(tlsf)

    tlsf_dataset_path = Path("../TLSF/" + dataset)
    for file in sorted(tlsf_dataset_path.glob("./*.tlsf")):
        cmd = "./../syfco-bin/syfco --format ltlxba-fin -m fully " + str(file.absolute())
        arch = subprocess.check_output(cmd, shell=True)
        # print(str(arch))
        if "Syntax Error" in str(arch):
            print(file.absolute())
        # os.system(cmd)

def transform_tlsf(dataset: str, file: Path) -> str:
    part_file = file.parent / f"{file.stem}.part"
    filename = f"{file.stem}"
    formula_str = file.read_text()
    if dataset.find ("Random") or dataset.find("Patterns"):
        formula_str = formula_str.replace(" & ", " && ")
        formula_str = formula_str.replace(")&", ") &&")
        formula_str = formula_str.replace("&&(", "&& (")
        formula_str = formula_str.replace(" | ", " || ")
    if formula_str.find(")->("):
        formula_str = formula_str.replace(")->(", " ) -> ( ")
    partition_str = part_file.read_text()
    ins_outs = partition_str.split('\n')
    if '' in ins_outs:
        ins_outs.remove('')
    assert (len(ins_outs) == 2)
    ins = ins_outs[0]
    ins_vars = ins.split(' ')[1:]

    outs = ins_outs[1]
    outs_vars = outs.split(' ')[1:]

    tlsf_info = "INFO {\n"
    tlsf_info += "  TITLE:       \""+ filename +"\"\n"
    tlsf_info += "  DESCRIPTION: \""+ dataset +"\"\n"
    tlsf_info += "  SEMANTICS:   Finite,Moore\n"
    tlsf_info += "  TARGET:      Moore\n"
    tlsf_info += "}\n"
    tlsf_info += "\n"

    tlsf_main = "MAIN {\n"
    tlsf_main += "\n"

    tlsf_ins = "  INPUTS {\n"
    for in_var in ins_vars:
        tlsf_ins += "    " + in_var + ";\n"
    tlsf_ins += "  }\n"
    tlsf_ins += "\n"

    tlsf_outs = "  OUTPUTS {\n"
    for out_var in outs_vars:
        tlsf_outs += "    " + out_var + ";\n"
    tlsf_outs += "  }\n"
    tlsf_outs += "\n"

    tlsf_guarantees = "  GUARANTEES {\n"
    tlsf_guarantees += "    " + formula_str + ";\n"
    tlsf_guarantees += "  }\n"

    tlsf_main += tlsf_ins + tlsf_outs + tlsf_guarantees
    tlsf_main += "\n"
    tlsf_main += "}"

    tlsf = tlsf_info + tlsf_main
    return tlsf


if __name__ == "__main__":
    datasets_ls = []
    datasets_ls.append("Patterns/GFand")
    datasets_ls.append("Patterns/Uright")
    datasets_ls.append("Random/Lydia/case_03_50")
    datasets_ls.append("Random/Lydia/case_04_50")
    datasets_ls.append("Random/Lydia/case_05_50")
    datasets_ls.append("Random/Lydia/case_06_50")
    datasets_ls.append("Random/Lydia/case_07_50")
    datasets_ls.append("Random/Lydia/case_08_50")
    datasets_ls.append("Random/Lydia/case_09_50")
    datasets_ls.append("Random/Lydia/case_10_50")
    datasets_ls.append("Random/Syft/syft_1")
    datasets_ls.append("Random/Syft/syft_2")
    datasets_ls.append("Random/Syft/syft_3")
    datasets_ls.append("Random/Syft/syft_4")
    datasets_ls.append("Random/Syft/syft_5")
    datasets_ls.append("Two-player-Game/Double-Counter/System-first")
    datasets_ls.append("Two-player-Game/Single-Counter/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_01/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_02/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_03/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_04/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_05/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_06/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_07/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_08/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_09/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_10/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_11/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_12/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_13/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_14/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_15/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_16/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_17/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_18/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_19/System-first")
    datasets_ls.append("Two-player-Game/Nim/nim_20/System-first")
    for datasets in datasets_ls:
        transform(datasets, "../TLSF")
