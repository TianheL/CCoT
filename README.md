# CCoT
Unoffical implementation of Compositional Chain-of-Thought Prompting for Large Multimodal Models


Scene Graph:
```json
[
  {
    "object": "man",
    "attributes": ["standing", "one leg raised", "arm extended"],
    "relationships": {
      "throwing": "frisbee"
    }
  },
  {
    "object": "frisbee",
    "attributes": ["in motion", "held by man"],
    "relationships": {
      "being thrown by": "man"
    }
  },
  {
    "object": "grass",
    "attributes": ["green", "outdoor"]
  }
]
```
Final answer:
```
(C)
```
