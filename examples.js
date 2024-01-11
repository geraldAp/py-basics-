// main function to be used for console logs
function debug(tag, outputVal) {
  console.log(`${tag} : ${outputVal}`);
}
// variables
var x = 5; //int
var y = 2.5;
debug("value of x", x);

// booleans
var is_student = true;
debug("is this a student ", is_student);

// basic math operators
var sum, dif, product, quotient, remainder;
sum = x + y;
dif = x - y;
product = x * y;
quotient = x / y;
debug("sum", sum);
debug("dif", dif);
debug("product", product);
// # to prevent from floating type casting a floating point number decimal to int
debug("qou", parseInt(quotient));

// modulo
remainder = 13 % 5;
debug("remainder", remainder);

// casting boolean to string
var this_to_string = true;
debug("is this a string", String(this_to_string));

// determine data types
var theStringType = "the string type";
debug("type of this is ", typeof theStringType);

/* if statement */
let age = 90;
if (age >= 18 && age < 65) console.log("you are an adult");
else if (age >= 65) console.log("you are a senior citizen");
else console.log("you are a minor");

// using and / or
var is_sunny, is_weekend;
is_sunny = true;
is_weekend = true;

if (is_sunny && is_weekend) console.log("lets go to the beach");
else if (is_sunny || is_weekend) console.log("no work today");
else console.log("let's go to work");

//  comparison operators
var a, b, z, k;
a = 10;
b = 20;

if (a > b) console.log(`${a} is greater than ${b}`);
if (a < b) console.log(`${a} is less than ${b}`);
if (a === b) console.log(`${a} is equal to ${b}`);

z = 5;
var is_greater_than_or_equal = z >= 5;
debug("is_greater_than_or_equal", is_greater_than_or_equal);

k = 5.0; // floating point
var is_not_equal = k != 5;
debug("is not equal", is_not_equal);

// inverting bools usually used in a toggle
var is_teacher = true;
var is_teacher_not = !is_teacher;

debug("is_teacher_not (inverted value),", is_teacher_not);

/*DATA STRUCTURES*/
// ARRAYS
let my_list = [1, 2, 3, 4, 5, 6, 7, 8, 8, 2, 2, 5];

// append an item to the array
my_list.push(9);

debug("appended item in list", my_list);
debug("my_list", my_list[0]);
// the last item the difference in comparison with js
debug("my_list", my_list[my_list.length - 1]);

// removing duplicates from arrays
var unique_array = [...new Set(my_list)];
debug("unique list", unique_array);

// tuples in js
var myTuple = [1, "hello", true, true];

var unique_tuple = [...new Set(myTuple)];

debug("unique Tuple", unique_tuple);

// objects in js
const my_object = { name: "bob", age: 18 };
debug("name", my_object.name);
debug("age", my_object["age"]);
// modifying
my_object["name"] = "chris";

// adding a new key-value pair
my_object.job = "fake life developer";
debug("job", my_object["job"]);

// remove key value pair
delete my_object.job;
debug("my object ", my_object.name);
console.log(my_object);

// for loops
numbers = [0, 1, 2, 4, 7, 34, 3543, 123, 657];

for (number of numbers) {
  debug("number ", number);
  if (number > 30 && number <= 300)
    console.log("number is greater than 30 or les than or equal to 300 ");
  else if (number > 300) console.log("number is greater than 300");
  else console.log("number is less than 30");
}
// while loop
let count = 0;
while (count < 5) {
  debug("while loop count", count);
  count++;
}

/*FUNCTIONS AND MODULES */

// functions without parameters
function sayHello() {
  console.log("hello");
}

sayHello();

// functions with params
function sayHello2(name) {
  console.log(`hello ${name.charAt(0).toUpperCase() + name.slice(1)}`);
}

sayHello2('yaro')
sayHello2('chris')    
sayHello2('richmann')  

/* CLASSES*/

class Dog {
  constructor(name, age){
    this.name = name;
    this.age = age;
  }

  bark(){
    console.log('woof')
  }
}

var my_dog = new Dog('fido', 3)
debug('my dog', my_dog.name)
my_dog.bark()

/*FILE HANDLING */
const fs = require('fs');
const filename = 'example2.txt'
let data = 'hello world this is a text file \n hjgdgshjfkdshfgvdskhvffhysvfskdj \njbdhasgdhdfgshavdgshdvgshcvghdvhvshjsdgfvjh \n djygfydskghafgagfyuyjgfihakfhfj\n '

// writing to the file synch
fs.writeFileSync(filename, data)


// reading the file asynch 
// way 1
fs.readFile(filename, 'utf-8', (err, data)=>{
  if (err) throw console.log(err);
  console.log(data)

})
//way 2
const asyncfs = require('fs/promises') 
async function readFile(){
  try {
    const data = await asyncfs.readFile(filename, 'utf-8')
    console.log(data)
  } catch (error) {
    console.log(error)
  }
}
readFile()

// reading a single line 
const readline = require('readline'); 
const file = readline.createInterface({ 
  input: fs.createReadStream(filename), 
  output: process.stdout, 
  terminal: false
}); 

file.on('line', (line) => { 
  console.log(line); 
});
