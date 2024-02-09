# NoSQLInjection
Before exploiting the NoSQL injection, there are MongoDB operators that we need to be familiar with that are heavily used in the injections, which are:

* `$eq` - matches records that equal to a certain value
* `$ne` - matches records that are not equal to a certain value
* `$gt` - matches records that are greater than a certain value.
* `$where` - matches records based on Javascript condition
* `$exists` - matches records that have a certain field
* `$regex` - matches records that satisfy certain regular expressions.

```txt
http://example.thm.labs/search?username=admin&role[$ne]=user
```