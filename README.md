# Dev-Elements Static Blog

I needed some place to stick my thoughts.

## Operation

There are two branches here, `main`, and `gh-pages`.

The former stores the static [Pelican](https://docs.getpelican.com/en/4.9.1/index.html) site along with everything you need to build it.

The latter stores just the `output` folder that is handed to the pages web service.

## Deployment

- Build content with `pelican content`
- Check to make sure everything is working with `pelican --listen`
- Add the output folder to the repo `git add output` and `git commit -m "my change"`
- Deploy with `git subtree push --prefix output origin gh-pages`


git push origin --delete gh-pages

git merge -s subtree --prefix output origin gh-pages --allow-unrelated-historie

git merge -s subtree -Xsubtree="$prefix" output/gh-pages --allow-unrelated-histories