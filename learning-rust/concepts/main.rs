// Concept: Main function is alwalys the fist code that runs in a Rust Program
fn main() {
    println!("Hello Macro"); // '!' = Rust macro != Function

    let x = 12;

    println!("{x}");

    let t = (12, 13.5, true);

    let (x, y, z) = t;

    println!("({x}, {y}, {z})");

    let first_element = t.0; // similar to 't[0]' in another languages. 0 is the index

    println!("{x} is equal to {first_element}");

    let a = [1, 2, 3, 4, 5];
    let first_element = a[0];
    println!("{first_element}");

    let x = {
        let y = 9;
        let z = 7;
        y + z
    };

    print_integers(x);

    let x = is_odd(4);
    println!("4 is odd {x}");
    let x = is_odd(5);
    println!("5 is odd {x}");

    let x = if is_odd(5) { "5 is odd" } else { "never" };

    println!("{x}");

    let mut counter = 0;
    let mut x = 1;
    let four_fat = loop {
        counter += 1;
        x *= counter;
        if counter == 4 {
            break x;
        }
    };

    print_integers(four_fat);

    for element in a {
        print_integers(element);
    }

    println!("In Range");
    for index in 0..=4 {
        print_integers(index);
    }
    println!("In Range (including 4)");
}

fn is_odd(i: i32) -> bool {
    if i % 2 == 0 {
        return false;
    }
    return true;
}

fn print_integers(i: i32) {
    println!("{i}");
}
