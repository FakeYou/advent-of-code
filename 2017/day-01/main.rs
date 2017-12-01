use std::path::Path;
use std::fs::File;
use std::error::Error;
use std::io::prelude::*;

fn main() {
	// Read the input file
	let path = Path::new("input.txt");
	let display = path.display();

	let mut file = match File::open(&path) {
		Err(why) => panic!("Couldn't open {}: {}", display, why.description()),
		Ok(file) => file,
	};

	let mut input = String::new();
	match file.read_to_string(&mut input) {
		Err(why) => panic!("Couldn't read {}: {}", display, why.description()),
		Ok(_) => (),
	};

	// create an array of bytes
	let numbers = input.as_bytes();
	let len = numbers.len();
	let mut i = 0;
	let mut total = 0;

	// loop through all bytes and check if it matches the next one
	while i < len - 1 {
		if numbers[i] == numbers[i + 1] {
			// cast the byte to an int and add it to the total
			total += (numbers[i] as u64) - 48;
		}

		i += 1;
	}

	// Special check for the loop-around
	if numbers[0] == numbers[len - 1] {
		total += (numbers[0] as u64) - 48;
	}

	print!("Answer part 1: {}\n", total);

	i = 0;
	total = 0;

	while i < len {
		if numbers[i] == numbers[(i + (len / 2)) % len] {
			total += (numbers[i] as u64) - 48;
		}

		i += 1;
	}

	print!("Answer part 2: {}\n", total);
}