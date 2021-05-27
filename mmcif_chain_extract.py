    
import argparse
import os

def select_chain(ciffile,chain_selected,chain_pdb):
    if os.path.exists(ciffile) and os.path.isfile(ciffile):
        with open(ciffile,"r") as fread:
            ROW="{RECORD:<6}{SERIAL:>5} {NAME:^4}{ALTLOC:1}{RESNAME:>3} {chain_selectedID:1}{RESSEQ:>4}{ICODE:1}   {X_COORD:>8}{Y_COORD:>8}{Z_COORD:>8}{OCCUPANCY:>6}{TEMPFACTOR:>6}          {ELEMENT:>2}{CHARGE:<2}"
            atoms=[x.split() for x in fread.read().split("\n") if x and ("ATOM " in x or "HETATM " in x)]

            pdbmap="\n".join([
                ROW.format(
                    RECORD=x[0],
                    SERIAL=x[1],
                    NAME=x[3],
                    ALTLOC=x[4].replace(".",""),
                    RESNAME=x[5],
                    chain_selectedID=chain_pdb,
                    RESSEQ=x[8],
                    ICODE="",
                    X_COORD=x[10],
                    Y_COORD=x[11],
                    Z_COORD=x[12],
                    OCCUPANCY=x[13],
                    TEMPFACTOR=x[14],
                    ELEMENT=x[3][0],
                    CHARGE=""
                )
                if len(x[3])<3 else
                ROW.format(
                    RECORD=x[0],
                    SERIAL=x[1],
                    NAME=" "+x[3],
                    ALTLOC=x[4].replace(".",""),
                    RESNAME=x[5],
                    chain_selectedID=chain_pdb,
                    RESSEQ=x[8],
                    ICODE="",
                    X_COORD=x[10],
                    Y_COORD=x[11],
                    Z_COORD=x[12],
                    OCCUPANCY=x[13],
                    TEMPFACTOR=x[14],
                    ELEMENT=x[3][0],
                    CHARGE=""
                )
                for x in atoms if len(x)>=20 and x[6]==chain_selected
            ])
            return pdbmap
    else:
        return "ciffile error"

if __name__=="__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("ciffile",help="PATH to mmcif file")
    parser.add_argument("chain",help="CHAIN to extract from mmciffile")
    parser.add_argument("output_chain",help="Output PDB file chain ID")
    args=parser.parse_args()

    output=select_chain(args.ciffile,args.chain,args.output_chain)
    print(output)
