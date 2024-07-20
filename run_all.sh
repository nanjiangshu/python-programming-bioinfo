SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || exit 1

bash exercises/build_all.sh ; bash lectures/build_all.sh ; bash assignment/build_all.sh ; ./copytowebapp2.sh
