# !/usr/bin/sh

clean () {
    rm -rf dist
    rm -rf scytale.egg-info
    rm -rf VERSION
    rm -rf build
    echo "DONE"
}

upload () {
    value=$(<VERSION)
    tar -cvf "scytale${value}.tar.gz" scytale
    python3 setup.py sdist bdist_wheel
    twine upload dist/*
}

case $1 in
    upload)
        upload
        ;;
    clean)
        clean
        ;;
    *)
        echo "ERROR: INVALID COMMAND"
        ;;
esac
