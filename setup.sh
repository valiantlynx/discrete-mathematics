# run using docker
docker build -t discrete-mathematics-image .
docker run --name discrete-mathematics-container -d -p 11434:11434 -p 8000:8000 -v $(pwd):/code discrete-mathematics-image

#connect to turborepo
git subtree add --prefix=apps/discrete-mathematics https://github.com/valiantlynx/discrete-mathematics.git main --squash
git subtree pull --prefix=apps/discrete-mathematics https://github.com/valiantlynx/discrete-mathematics.git main --squash
git subtree push --prefix=apps/discrete-mathematics https://github.com/valiantlynx/discrete-mathematics.git main
