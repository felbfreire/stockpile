stockpile implements a client for managing json files as a text-based db.

Author: Felipe Freire - felbfreire
repo: https://github.com/felbfreire/stockpile.git

<h2>Write ..</h2>

```bash
$ python stockpile write_data foo=bar
```

<h2>Read ..</h2>

```bash
$ python stockpile read_data

  foo: bar
```

<h2>Insert an object ..</h2>

```bash
$ python stockpile write_object a_key foo=bar

$ python stockpile read_data

  foo: bar
  a_key : {'foo': 'bar'}
```

<h2>Update any object with update_object</h2>

```bash
$ python stockpile update_object a_key foo=BEER

$ python stockpile read_data

  foo: bar
  a_key : {'foo': 'BEER'}
```
