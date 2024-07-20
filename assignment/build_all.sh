SCRIPT_DIR=$(dirname "$(realpath "$0")")
cd "$SCRIPT_DIR" || exit 1

for file in $(find . -depth 1 -name "*.ipynb" | grep -v bak); do
    jupyter nbconvert --to html --EmbedImagesPreprocessor.embed_images=True $file
done

