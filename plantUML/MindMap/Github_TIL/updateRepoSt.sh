#!/bin/sh
case `uname -s` in
    Linux)
        echo 'OSはLinuxです。macで実行してください。'
        exit;;
    Darwin)
        echo 'plantumlを実行します。'
        break;;
    *)
        echo 'OSがわかりません'
        exit;;
esac

plantuml RepositoryStructure.puml &&\
plantuml RepositoryStructureJ.puml &&\
mv  *.png ../../../ &&\
tree ../../../ > TILtree.txt &&\
mv TILtree.txt ../../../


