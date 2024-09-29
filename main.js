const { GoogleGenerativeAI } = require("@google/generative-ai");
const fs = require('fs');
const pdf = require('pdf-parse');

// Initialize the Google Generative AI client
const genAI = new GoogleGenerativeAI("AIzaSyCbzwmZgzmrz_YajlMLXOhTc-GvVo6FfYI");

async function extractTextFromPDF(pdfPath) {
    const dataBuffer = fs.readFileSync(pdfPath);
    const data = await pdf(dataBuffer);
    return data.text; // Extracted text
}

async function extractTextFromFile(filePath) {
    return fs.promises.readFile(filePath, 'utf8');
}

async function generateSummary(text) {
    // Get the generative model
    const model = genAI.getGenerativeModel({ model: "gemini-1.5-flash" });

    try {
        // Generate content using the model
        const result = await model.generateContent({
            contents: [
                { role: "user", parts: [ { text: `Provide a detailed summary of the paragraphs  that is structured in a hierarchical format. Break down the information as much as possible into multiple levels of subtopics. Use indentation to represent the levels, ensuring that The top level contains main headings with no indentation.Each subheading should be indented with 2 spaces, and further breakdowns should be indented 4 spaces, 6 spaces, and so on.Continue breaking down topics into smaller subtopics where applicable let the  main heading be in all upercase.dontuse any numbers to represent the points use only indentation.give as many level of indentation as possible.even if there is comma if it can be indentended again then that also indententt it to a meaning full one.if possible to indent till a getting a word then indent it also .give the detailed summary withsimple sentence containg 2 or 3 words.give manysubheading.give with atleast 5 level of indentation.give in such way that the one level of indentation's is related to the its parent indentation.dont giverandomlevel of indentation.give sub heading in one level and its content in next level of indentation.it is very important to have atleast 7 level of indentation(if more than 2 paragraph) .breakdown sentence in a such a way that there should not be more than 3 words in a sentence.dont provide separete section for summary: ${text}` }] }
            ]
        });

        // Write the summary to a text file
        fs.writeFileSync('summary.txt', result.response.text());
        console.log('Summary saved to summary.txt');
    } catch (error) {
        console.error("Error generating summary:", error);
    }
}

async function processFile(filePath, fileType = 'pdf') {
    try {
        let text;
        if (fileType === 'pdf') {
            text = await extractTextFromPDF(filePath);
        } else if (fileType === 'txt') {
            text = await extractTextFromFile(filePath);
        } else {
            throw new Error("Unsupported file type. Please provide 'pdf' or 'txt'.");
        }
        await generateSummary(text);
    } catch (error) {
        console.error("Error processing file:", error);
    }
}

// Replace 'your-file.pdf' or 'your-file.txt' with the path to your file
// Replace 'pdf' with 'txt' if processing a text file
processFile('data.txt', 'txt'); // for PDF files
// processFile('your-file.txt', 'txt'); // for text files
