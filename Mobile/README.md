#  Mobile Software Development Class Notes
> Note system:
> - Midterm: 30%
> - Final: 40%
> - Assignments: 30%

## Hello World
```java
fun main() {
    println("Hello World")
}

fun main(args: Array<String>) {
    println("Hello World")
}

fun main() = println("Hello World")
```

## Operators
### Mathemathical Operators
- '+', '-', '*', '/', '%'
```java
val a = 10
val b = 20
val c = a + b // 30
val d = a - b // -10
val e = a * b // 200
val f = a / b // 0
val g = a % b // 10
```

### Increment and Decrement Operators
- '++', '--'
```java
var a = 10
a++ // 11
a-- // 10
```

### Comparison Operators
- '==', '!=', '>', '<', '>=', '<='
```java
val a = 10
val b = 20
val c = a == b // false
val d = a != b // true
val e = a > b // false
val f = a < b // true
val g = a >= b // false
val h = a <= b // true
```

### Assignment Operators
- '=', '+=', '-=', '*=', '/=', '%='
```java
var a = 10
a += 5 // 15
a -= 5 // 10
a *= 5 // 50
a /= 5 // 10
a %= 5 // 0
```

### Equality Operators
- '&&', '||', '!'
```java
val a = 10
val b = 20

val c = a > 5 && b < 30 // true
val d = a > 5 || b > 30 // true
val e = !(a > 5) // false
```

### Numeric Operator Functions
- 'inc()', 'dec()', 'plus()', 'minus()', 'times()', 'div()', 'rem()'
```java
var a = 10
a.inc() // 11
a.dec() // 9
a.plus(5) // 15
a.minus(5) // 5
a.times(5) // 50
a.div(5) // 2
a.rem(5) // 0
```

## Data Types
### Integer Types

| Type | Size | Range |
|------|------|-------|
| Byte | 8 bits | -128 to 127 |
| Short | 16 bits | -32768 to 32767 |
| Int | 32 bits | -2^31 to 2^31-1 |
| Long | 64 bits | -2^63 to 2^63-1 |

### Floating Point Types

| Type | Size | Range |
|------|------|-------|
| Float | 32 bits | 1.40129846432481707e-45 to 3.40282346638528860e+38 |
| Double | 64 bits | 4.94065645841246544e-324 to 1.79769313486231570e+308 |

### Characters and Booleans

| Type | Size | Range |
|------|------|-------|
| Char | 16 bits | 0 to 65535 |
| Boolean | 1 bit | true or false |

### Type Casting
```java
val a: Int = 10
val b: Long = a.toLong()
```

### Underscores in Numeric Literals
```java
val a = 1_000_000
val b = 0xFF_EC_DE_5E
val c = 0b1101_1001_0001_1101
```

### Strings
```java
val a = "Hello World"
val b = "Hello" + "World"
val c = "Hello World".length // 11
val d = "Hello World"[0] // 'H'
val e = "Hello World".substring(6, 11) // "World"
val f = """Hello
           World""" // Multiline string
```

### String Concatenation
```java
val a = "Hello"
val b = "World"
val c = "$a $b" // "Hello World"
```

### String Templates
```java
val a = "Hello"
val b = "World"
val c = "$a ${b.length}" // "Hello 5"
```

### String Builder
```java
val a = StringBuilder()
a.append("Hello")
a.append("World")
val b = a.toString() // "HelloWorld"
```

## Variables
### Immutable Variables
```java
val a = 10
val b: Int = 20
```

### Mutable Variables
```java
var a = 10
var b: Int = 20
```

### Immutable vs Mutable
- Use immutable variables whenever possible
- Use mutable variables only when necessary
```java
val a = 10
var b = 20
a = 30 // Error
b = 40 // OK
```

### Type Inference
```java
var a = 10 // Int
var b = 20L // Long
var c = 30.0 // Double
var d = 40.0f // Float
var e = 'A' // Char
var f = "Hello" // String
var g = true // Boolean
var h: Int = 10 // Int
```

## Control Flow
### If Expression
```java
val a = 10
val b = 20
val c = if (a > b) a else b
if (a > b) {
    println("a is greater than b")
} else {
    println("b is greater than a")
}

if (a > b) println("a is greater than b")
else if (a < b) println("a is less than b")
else println("a is equal to b")
```

### When Expression
```java
val a = 10
when (a) {
    10 -> println("a is 10")
    20 -> println("a is 20")
    else -> println("a is neither 10 nor 20")
}
```

### For Loop
```java
for (i in 1..10) {
    println(i)
}

for (i in 1 until 10) {
    println(i)
}

for (i in 10 downTo 1) {
    println(i)
}

for (i in 1..10 step 2) {
    println(i)
}
```

### While Loop
```java
var i = 1
while (i <= 10) {
    println(i)
    i++
}
```

### Repeat Loop
```java
repeat(10) {
    println("Hello")
}
```

## Lists and Arrays
### Lists
- Lists are or
- List elements can be accessed programmatically using indices
- List elements can occur multiple times
```java 
val a = listOf(1, 2, 3, 4, 5)
val b = mutableListOf(1, 2, 3, "4", 5)
b.remove(3)
```

### Arrays
- Arrays store multiple items
- Array elements can be accessed programmatically using indices
- Array elements are mutable
- Arrays have fixed size
```java
val a = arrayOf(1, "2", "3", 4, 5)
val b = intArrayOf(1, 2, 3)
val c = intArrayOf(4, 5, 6)
val d = b + c // [1, 2, 3, 4, 5, 6]
```

## Null Safety
- In kotlin, null is not allowed by default
- You can assign null to a variable by adding a '?' to the type
```java
var a: Int? = null
var b: Int = null // Error
```

### Elvis Operator
- Elvis operator is used to provide a default value when a variable is null
```java
val a: Int? = null
val b = a ?: 0 // a if not null, 0 otherwise
```

### Safe Calls
- Safe calls are used to call a method on a nullable variable
```java
val a: Int? = null
val b = a?.inc() // null
```

### Not Null Assertion
- Not null assertion is used to tell the compiler that a variable is not null
```java
val a: Int? = null
val b = a!!.inc() // Error
```

## Args in main
```java
fun main(args: Array<String>) {
    println(args[0])
}
```

## Functions
### Function Declaration
```java
fun add(a: Int, b: Int): Int {
    return a + b
}
```

### Function Expression
```java
fun add(a: Int, b: Int) = a + b
```

### Default Arguments
```java
fun add(a: Int, b: Int = 0) = a + b
```

### Named Arguments
```java
fun add(a: Int, b: Int) = a + b
add(b = 10, a = 20)
```

## Unit
- Unit is a type in kotlin that represents the absence of a value
- Unit is similar to void in Java
```java
fun add(a: Int, b: Int): Unit {
    println(a + b)
}
```

## Lambda Expressions
```java
val add = { a: Int, b: Int -> a + b }
val res = add(10, 20) // 30
```

## Function Types
```java
val add: (Int, Int) -> Int = { a, b -> a + b }
val sub: (Int, Int) -> Int = { a, b -> a - b }
val res1 = add(10, 20) // 30
val res2 = sub(10, 20) // -10
```

## Higher Order Functions
```java
fun add(a: Int, b: Int) = a + b
fun sub(a: Int, b: Int) = a - b

fun calc(a: Int, b: Int, op: (Int, Int) -> Int): Int {
    return op(a, b)
}

val res1 = calc(10, 20, ::add) // 30
val res2 = calc(10, 20, ::sub) // -10
```

## Class
### Defining a Class
```java
class Person {
    var name: String = ""
    var age: Int = 0
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}
```

### Creating an Object
```java
val person = Person()
person.name = "John"
person.age = 30
person.greet()
```

### Encapsulation
```java
class Person {
    var name: String = ""
        get() = field.toUpperCase()
        set(value) {
            field = value.toLowerCase()
        }
    var age: Int = 0
        private set
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

val person = Person()
person.name = "John" // john
println(person.name) // JOHN
person.age = 30 // Error
```

### Constructors
```java
class Person(name: String, age: Int) {
    var name: String = name
    var age: Int = age
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

val person = Person("John", 30)
person.greet()
```

### Init Block
```java
class Person(name: String, age: Int) {
    var name: String = name
    var age: Int = age
    init {
        println("Person object created")
    }
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

val person = Person("John", 30) // Person object created
person.greet()
```

### Secondary Constructors
```java
class Person {
    var name: String = ""
    var age: Int = 0
    constructor(name: String, age: Int) {
        this.name = name
        this.age = age
    }
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

val person = Person("John", 30)
person.greet()
```

## Visibility Modifiers

| Modifier | Description |
|----------|-------------|
| public | Visible everywhere |
| private | Visible inside the class only |
| protected | Visible inside the class and its subclasses |
| internal | Visible inside the module |

```java
class Person {
    private var name: String = ""
    protected var age: Int = 0
    internal var address: String = ""
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

val person = Person()
person.name = "John" // Error
person.age = 30 // OK
person.address = "New York" // OK
```

## Properties
### Getters and Setters
```java
class Person {
    var name: String = ""
        get() = field.toUpperCase()
        set(value) {
            field = value.toLowerCase()
        }
    var age: Int = 0
        private set
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

val person = Person()
person.name = "John" // john
println(person.name) // JOHN
person.age = 30 // Error
```

## Inheritance
### Defining a Subclass
```java
open class Person {
    var name: String = ""
    var age: Int = 0
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

class Student: Person() {
    var rollNo: Int = 0
    fun study() {
        println("Student is studying")
    }
}

val student = Student()
student.name = "John"
student.age = 30
student.rollNo = 100
student.greet()
student.study()
```

### Secondary Constructors in Subclass
```java
open class Person {
    var name: String = ""
    var age: Int = 0
    constructor(name: String, age: Int) {
        this.name = name
        this.age = age
    }
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

class Student: Person {
    var rollNo: Int = 0
    constructor(name: String, age: Int, rollNo: Int): super(name, age) {
        this.rollNo = rollNo
    }
    fun study() {
        println("Student is studying")
    }
}

val student = Student("John", 30, 100)
student.greet()
student.study()
```

### Overriding Methods
```java
open class Person {
    open fun greet() {
        println("Hello, I am a person")
    }
}

class Student: Person() {
    override fun greet() {
        println("Hello, I am a student")
    }
}

val student = Student()
student.greet() // Hello, I am a student
```

## Interfaces
### Defining an Interface
```java
interface Person {
    var name: String
    var age: Int
    fun greet()
}

class Student: Person {
    override var name: String = ""
    override var age: Int = 0
    override fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

val student = Student()
student.name = "John"
student.age = 30
student.greet()
```

### Implementing Multiple Interfaces
```java
interface Person {
    var name: String
    var age: Int
    fun greet()
}

interface Student {
    var rollNo: Int
    fun study()
}

class CollegeStudent: Person, Student {
    override var name: String = ""
    override var age: Int = 0
    override var rollNo: Int = 0
    override fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
    override fun study() {
        println("Student is studying")
    }
}

val student = CollegeStudent()
student.name = "John"
student.age = 30
student.rollNo = 100
student.greet()
student.study()
```

## Abstract Classes
### Defining an Abstract Class
```java
abstract class Person {
    abstract var name: String
    abstract var age: Int
    abstract fun greet()
}

class Student: Person() {
    override var name: String = ""
    override var age: Int = 0
    override fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

val student = Student()
student.name = "John"
student.age = 30
student.greet()
```

## Extensions
### Adding Functions to Existing Classes
```java
fun String.greet() {
    println("Hello, $this")
}

"John".greet() // Hello, John
```

### Adding Properties to Existing Classes
```java
val String.length: Int
    get() = this.length

val len = "Hello".length // 5
```

## Object/Singleton
### Object Declaration
```java
object Person {
    var name: String = ""
    var age: Int = 0
    fun greet() {
        println("Hello, my name is $name and I am $age years old")
    }
}

Person.name = "John"
Person.age = 30
Person.greet()
```

### Object Singleton
- Object declaration is used to create a singleton
- Singleton is a design pattern that restricts the instantiation of a class to one object
```java
fun main() {
    println(Utils.add(10, 20))
    println(Utils.sub(10, 20))
}

object Utils {
    fun add(a: Int, b: Int) = a + b
    fun sub(a: Int, b: Int) = a - b
}
```