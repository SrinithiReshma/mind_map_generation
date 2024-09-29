const fs = require('fs');

// Read the input file
fs.readFile('summary.txt', 'utf8', (err, data) => {
    if (err) {
        console.error('Error reading file:', err);
        return;
    }

    // Remove all '*' and '#' characters
    const cleanedData = data.replace(/[*#]/g, '');

    // Write the cleaned data to a new file
    fs.writeFile('cleaned_output.txt', cleanedData, (err) => {
        if (err) {
            console.error('Error writing file:', err);
        } else {
            console.log('Cleaned file saved as cleaned_output.txt');
        }
    });
});
