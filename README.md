# Cryptography Projects 🔑🔒
All and any cryptography related tools or projects.

## 1. Find-Random-Int
- Purpose is to "Predict" the third number being generated given the first two "random" numbers
- the function exploited is nextInt() in the Java Random class: <br />
<code> int n1 = rand.nextInt();  </code> <br />
<code> int n2 = rand.nextInt();  </code> <br />
<code> int n3 = rand.nextInt();</code> <-- find this

## 2. Multi Time Pad
- This problem is from Dan Boneh's CS255 course at Stanford University.
- Details of problem can be found [here](https://crypto.stanford.edu/~dabo/courses/OnlineCrypto/slides/02-stream-v2-annotated.pdf)
- ciphertext was generated with a given encrypted key
