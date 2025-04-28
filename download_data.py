from huggingface_hub import hf_hub_download
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--langs", nargs="+", help="List of languages that you want to download blimp minimal pairs for")

args = parser.parse_args()
print(args.langs)

for l in args.langs:
  hf_hub_download(repo_id="jumelet/multiblimp", filename=f"{l}/data.tsv", repo_type="dataset", local_dir='hf_cache/')
