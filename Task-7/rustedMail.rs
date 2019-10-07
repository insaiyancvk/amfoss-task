extern crate regex;

use regex::Regex;

fn main()
	 {
    use std::io::{stdin,stdout,Write};


    let mut mail=String::new();


    print!("Enter the E Mail to be checked : ");


    let _=stdout().flush();


    stdin().read_line(&mut mail).expect("error: unable to read user input");


	if Regex::new(r"^[a-zA-Z0-9]+@[a-z][.]?[a-z]*").unwrap().is_match(&mut mail) == true
	{

	    println!("The E-Mail entered is valid");

	}
	else
	{

	    println!("The entered E Mail is not valid");

	}
}
