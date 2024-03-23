use rand::Rng;
use std::{cmp::Ordering, io}; // importing libraries

fn main() {
    println!("Guess the number!"); // calling a macro

    // range expression = start..=end
    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Please input your guess:");

        // 'let' statement to create variables. Default is 'immutable'
        // 'mut' makes mutable
        // ::new = associated function = is a function that’s implemented on a type
        let mut guess = String::new();

        io::stdin()
            .read_line(&mut guess) // calling a function to read the user input
            .expect("Failed to read line");

        let guess = guess.trim();

        println!("You guessed: {guess}"); // interpolation of strings using {}

        let guess: u32 = match guess.parse() {
            Ok(num) => num,
            Err(_) => continue,
        };

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small :("),
            Ordering::Equal => {
                println!("You Win :)");
                break;
            }
            Ordering::Greater => println!("Too big :0"),
        }
    }
}
