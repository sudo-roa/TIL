#!/bin/sh

plantuml RepositoryStructure.puml &&\
plantuml RepositoryStructureJ.puml &&\
mv  *.png ../../../ &&\
tree ../../../ > TILtree.txt &&\
mv TILtree.txt ../../../


