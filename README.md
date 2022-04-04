# Enumify
> A quick way to write documented Enums, or Enums with member values


## Install

`pip install enumify`

## What is Enumify?

Enumify was built on an idea of how could I be the absolute laziest at declaring Enums, honestly!

I didn't enjoy the idea of how I would need to re-type out member names if I just wanted them to be a 1:1, such as the following:

```
import enum

class DaysOfWeek(enum.Enum):
    MONDAY = "monday"
    TUESDAY = "tuesday"
    WEDNESDAY = "wednesday"
```

There is of course, an alternative that lives in `fastcore`, specifically the `mk_class`, which annotates like the following:
```python
from fastcore.basics import mk_class
mk_class("DaysOfWeek", {o:o.lower() for o in ["MONDAY", "TUESDAY", "WEDNESDAY"]})
```

But I didn't like that the `DaysOfWeek` class was permeable as it was not a true `Enum`, and I had a side goal of also making the enum members be **documented**.

As a result, this is our finished conversion of that previous enum:

```
from enumify import enumify, Member

@enumify
class DaysOfWeek:
    MONDAY:Member
    TUESDAY:Member
    WEDNESDAY:Member
```


    ---------------------------------------------------------------------------

    AttributeError                            Traceback (most recent call last)

    Input In [2], in <module>
          1 from enumify import enumify, Member
          3 @enumify
    ----> 4 class DaysOfWeek:
          5     MONDAY:Member
          6     TUESDAY:Member


    File ~/local/zach/enumify/enumify/enumify.py:92, in enumify(cls, interactive)
         90 if cls is None:
         91     return partial(enumify, interactive=interactive)
    ---> 92 return wrap(cls, interactive)


    File ~/local/zach/enumify/enumify/enumify.py:89, in enumify.<locals>.wrap(cls, interactive)
    ---> 89 def wrap(cls, interactive): return assign_annotations(cls, interactive)


    File ~/local/zach/enumify/enumify/enumify.py:38, in assign_annotations(cls, interactive)
         36         names.append([name, value])
         37     else:
    ---> 38         names.append([name, (value, getattr(cls, name))])
         39     keys.append(name)
         41 for name in d:


    AttributeError: type object 'DaysOfWeek' has no attribute 'MONDAY'


And we can see its set value below:

```
print(DaysOfWeek.MONDAY)
```

    monday


Thus we come to the two use-cases of `enumify`:
- Make Enum's whose member's values are the names of the members
- Make Enum's whose members can be *documented*

## How do I use it?

There are two supported "modes" for `enumify`, an interactive mode and a static mode. The static mode should be used when you're in environments such as VSCode or PyLint, where they can make use of documentation underneath a particular variable or member. 

Interactive mode should be if you are developing or working out of Jupyter Notebook for your enums.

What do I mean by this? Let's compare two examples.

### Interactive Mode

With interactive mode, we can not only use the `Member` or `Mem` notation to specify our self-named member, but we can also document that member with an assign:

```
@enumify(interactive=True)
class DaysOfWeek:
    MONDAY:Member = "The first day of the week"
    TUESDAY:Member = "The second day of the week"
    WEDNESDAY:Member = "The third day of the week"
```

And now these members will have affiliated documentation:

```
DaysOfWeek.MONDAY.__doc__
```




    'The first day of the week'



We can even document values that aren't `Member` type by specifying it's documentation last in the assign

```
@enumify(interactive=True)
class DaysOfWeek:
    MONDAY:Member = "The first day of the week"
    TUESDAY:int = 0, "Some number"
```

```
DaysOfWeek.TUESDAY.__doc__
```




    'Some number'



**BUT**, they will *not* have this documentation show when using IDE's such as VSCode. This is where static mode comes in.

### Static Mode

With static mode, we can still use the `Member` annotation, but we assume that the user will be working out of an IDE and instead rely on how IDE's can annotate variables.
{% include note.html content='If so, it will be impossible for Jupyter/Notebook users to pick up your documentation for the member' %}
Below is our complete `DaysOfWeek` example with this:

```
@enumify(interactive=False)
class DaysOfWeek:
    MONDAY:Member
    "The first day of the week"
    TUESDAY:Member
    "The second day of the week"
    WEDNESDAY:Member
    "The third day of the week"
```

```
DaysOfWeek.MONDAY
```




    <DaysOfWeek.MONDAY: 'monday'>



```
assert DaysOfWeek.MONDAY.__doc__ is None
```
