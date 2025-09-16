use std::io;

fn main() {
    let mut n = String::new();
    io::stdin()
        .read_line(&mut n)
        .expect("Failed to read line");
    let n: i32 = n.trim().parse().expect("Please type a number.");

    let mut counter = 0;
    while counter < n {
        let mut input = String::new();
        io::stdin()
            .read_line(&mut input)
            .expect("Failed to read line");
        let values: Vec<&str> = input.split(" ").collect();
        let x = values[0].trim();
        let y = values[1].trim();
        if y.len() <= x.len() {
            let end = x.len(); 
            let start = end - y.len(); 
            let contains = &x[start..end] == y;
            if contains {
                println!("encaixa");
            } else {
                println!("nao encaixa");
            }
        } else {
            println!("nao encaixa");
        } 
        counter += 1;
    }
}