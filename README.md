# MultiBLiMP

This is my modified implementation of [Jumelet et al. (2025) MultiBLiMP 1.0](https://arxiv.org/abs/2504.02768). Any bugs or errors are my own. 

The updates include:
* documentation on how to integrate the Hugging Face datasets into the pipeline
* example code for running multiblimp
* handling of model checkpoints


## Setup

You will need `minicons` installed. 

```
git clone https://github.com/catherinearnett/multiblimp
cd multiblimp
```

### Download Datasets

For all the languages you plan to evaluate, download them in to a directory inside `multiblimp/`, called `hf_cache`. Use the [ISO 639-3](https://en.wikipedia.org/wiki/ISO_639-3) code, e.g. `eng` for English, `tur` for Turkish, `rus` for Russian.

```
python download_data.py --langs eng tur rus

```

## Using MultiBLiMP

There are a few differences between the `eval_model` function and the original `lm_eval` from the [LM Evaluation Harness](https://github.com/EleutherAI/lm-evaluation-harness). Instead of `model_args`, there is a `model` argument. This should be a model on Hugging Face¹. I added a `--revision` flag, which allows you to add model step. Make sure to note the naming convention for the revisions for your model. For example, the Pythia models have their steps labelled as `step1000`, `step10000`, etc.


```
python scripts/lm_eval/eval_model.py 
        --model catherinearnett/B-GPT_en_nl_simultaneous #model name on huggingface
        --revision 10000 # #model checkpoint
        --data_dir hf_cache/eng/ # directory where you downloadded the dataset for the language you're evaluating on
        --src_dir multiblimp 
        --results_dir bgpt_multiblimp_results/ 
        --cache_dir hf_cache/ 
#        --hf_token hf_token #optional: if you're using a model that's uploaded privately
```

I have uploaded a script, `get_multiblimp_scores.py`, which provides an example of how to loop over multiple models, checkpoints, and languages. 

### Notes

¹ In order to run local models, you will need to adapt the `load_hf_model` function (or create a new function) in `src/lm_eval/load_model.py`.

## Citation

```
@article{jumelet2025multiblimp,
  title={MultiBLiMP 1.0: A Massively Multilingual Benchmark of Linguistic Minimal Pairs},
  author={Jumelet, Jaap and Weissweiler, Leonie and Bisazza, Arianna},
  journal={arXiv preprint arXiv:2504.02768},
  year={2025}
}
```
