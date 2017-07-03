# The legacy of (old) code

## Memory of first steps

When you started out coding, you heard that solving coding katas
can improve your skills.

So you searched the interwebs and found one
[here](http://codingdojo.org/kata/Bowling/).

It instructed to write tests but you came to learn coding, not testing.
You decided to write those pesky tests at the end.
All in all when you're done it might not be a bad idea to make sure it works.

So you got everything to work with blood, sweat and tears;
then wrote some tests.
Some of them failed, you corrected those and were so proud of your work
that you never ever looked at it again.

## Stirring up the past

Now that you have solved many more katas (many times)
and you know about unit testing and clean code principles
you decided instead to revisit an old solution of yours
and see if you can improve on it.

## What are you supposed to do?

Clone the repo from [here](https://github.com/whatever).
Make sure you can run the tests and they pass.
```
python tests.py -v
```
(Use version 3 of python)

Then refactor your code according to the clean code principles.

## Rules you decided to follow

* Always keep the existing tests passing
* Don't delete any tests
* Commit early commit often
* You can add new tests
* Only refactor code that is covered by tests
* If there are no tests for a specific case then write one
