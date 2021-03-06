# hunlp-scripts

Hungarian NLP pipeline for tokenization and sentence detection using `huntoken`, PoS-tagging using `hunpos`, morphological analysis using `hunmorph`, stem generation and 
heuristic stem seletion based on the PoS-tag with python scripts.

Created by Marton Mihaltz 

## Installation

1. clone this repo:  
`https://github.com/mmihaltz/hunlp-pipeline.git`

2. Run `setup.sh` to install python requirements (may require `sudo` depending on your setup)

3. Obtain the hunlp tools:  
- huntoken
- hunpos
- hunmorph

*Note*: You can get the all of the above with trained models in one package from:  
  https://bitbucket.org/mmihaltz/hun-tools-bin  
Please follow installation instructions in the README.

4. In `010.huntoken`, `011.hunmorph`, `011.hunpos-hunmorph` set the HUNTDIR variable to the directory that contains the tools in 3.

## Testing

Run:
```
./test.sh
```

If everything works right you will get an output file `test.txt.ana`, which should be more or less the same as to the included `test.txt.ana.expected`.
