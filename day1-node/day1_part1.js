import { createReadStream } from 'fs';
import { createInterface } from 'readline';

const main = async() => {
    const f = process.argv[2]  // filename
    console.log("Parsing input file: ", f);

    // Reading input file
    const fileStream = createReadStream(f);
    const rl = createInterface({
        input: fileStream,
        crlfDelay: Infinity
    });

    // Parsing input file and converting to list of integers
    var expenses = [];
    for await (const line of rl) {
        const n = parseInt(line);
        expenses.push(n);
    }

    const {first, second} =  await find2020(expenses);
    const product = first * second;
    console.log("Result: ", product);

};

/*
 * Core function of this task: Find two summands that add up to 2020
 */
const find2020 = async(list_of_expenses) => {
    for (var i = 0; i < list_of_expenses.length - 1; i++) {
        for (var k = i + 1; k < list_of_expenses.length; k++) {
            const summand1 = list_of_expenses[i];
            const summand2 = list_of_expenses[k];
            if (summand1 + summand2 == 2020) {
                console.log("Found match!");
                return {
                    first: summand1,
                    second: summand2
                }
            }
        }
    }

    // FIXME: Yeah, I know this sucks. But I know that there is a result ;-)
    return {
        first: null,
        second: null
    }
}

main().catch((err) => {
    console.error(err);
});