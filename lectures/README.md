# Lectures

This repo contains the lecture materials.

## Executable lectures

Located as `lecture_*.py` in the root directory

You can compile a lecture by running:

```
    cd lectures
    python execute.py -m lecture_01
```

which generates a `var/traces/lecture_01.json` and caches any images as appropriate.

## Frontend

If you need to tweak the Javascript:

Install (one-time):

```
    npm create vite@latest trace-viewer -- --template react
    cd trace-viewer
    npm install
```

Load a local server:

```
    cd trace-viewer
    npm run dev
```

view at `http://localhost:5173?trace=var/traces/lecture_01.json`

## Acknowledgements

This project is inspired by the course  *[Stanford CS336: Language Modeling from Scratch](https://github.com/stanford-cs336/spring2025-lectures)* . The overall structure of the course materials, as well as parts of the implementation design, draw from the ideas and framework presented in this course.
