# Petit Type System


This library is meant to be used as a backend to implement type exporter from python to another language.

In order to use it, you are supposed to implement the different handlers for the types you want to export.

Petit-ts is based on it, and is able to export any of current python types.

Petit-java is currently under development and will make the export of python types to Java available

The next step will be to build an GraphQL exporter

## Where to start ?

The libs works by using a store which has handlers for each type of data. To create a new type of store, you have to use `create_store_class`, this will return a factory, which can later be used to create an actual store, which will hold all of the informations of your different types.

Example:

```python
ts_raw_default_types: List[Tuple[Any, str]] = [
    (bool, "boolean"),
    (None, "void"),
    (NoneType, "undefined"),

    (null, "null"),
    (undefined, "undefined"),

    (int, "number /*int*/"),
    (float, "number /*float*/"),

    (str, "string"),
    (dict, "object"),
    (list, "any[]"),

    (List[Any], "any[]"),
    (List, "any[]"),
    (List[int], "number[]"),
    (List[str], "string[]"),

    # any's
    (object, "any"),
    (Any, "any"),
]


# TS-specifics
ts_export_token = 'export'

ts_class_handlers: List[Type[ClassHandler]] = [
    TSEnumHandler,
    TSDataclassHandler,
]

ts_basic_handlers: List[Type[BasicHandler]] = [
    TSUnionHandler,
    TSLiteralHandler,
    TSArrayHandler,
    TSMappingHandler,
    TSTupleHandler,
]

TSTypeStore = create_store_class(
    ts_export_token,
    struct_handler=TSStructHandler,
    basic_handlers=ts_basic_handlers,
    class_handlers=ts_class_handlers,
    basic_types=ts_raw_default_types,
)
```

This is an example taken from petit-ts

We have 3 types of handlers:

- BasicHandler
- ClassHandler
- StructHandler

### BasicHandler

A `BasicHandler` implements two methods:

#### should_handle(cls: Any) -> bool

This functions returns wether this Handler should actually handle the supplied object

#### build(cls: Any) -> Tuple[Optional[str], str]

This function builds the representation of your type in the target language, most of the time it will use the `store.get_repr(value)` expression.

It returns a Tuple[Optional[str], str] where the first value, is the name the exported type. In some langague you can return `None` and the type will be inlined.

For example Typescript supports it but Java doesn't.

The second value is the actual representation.

### ClassHandler

A `ClassHandler` implements 3 methods:

#### is_mapping() -> bool

This function tells the library if it should use the `StructRenderer` on the returned data or just use the result a the representation directly

For example, the `DataclassHandler` and the `PydanticHandler` use it in order to reduce the amount of code. 


#### should_handle

Like for the BaseHandler this method returns wether the handler should handle the supplied object.

#### build

This function returns, a string representation or a dict depending on if it's a mapping or not

### StructHandler

This handler implements the process of making structs for the target language.

A `StructHandler` implements 2 methods:

### make_struct

This methods returns a string representation of a given dict, or dict-like object.

### make_struct_inline

This does the same as the previous function but it does it inline.

For example, Typescript supports it but Java doesn't.

If you don't want to support this option or if the target language doesn't support it, you don't have to do anything.

### BasicTypes

We have the basic types and their string representation.

### Export token

For now we use an export token, it is used in order to export a type from a given class/module.


## Todo

Update the part where the generic classes are handled
