Dropzone.options.rrrDropzone = { // camel-ized version of the 'id'
    paramName: "file", // The name that will be used to transfer the file
    accept: function(file, done) {
        if (file.name == "potato.txt") {
            done("I see you... always");
        }
        else { done("Aight dawg, your file has been uploaded!"); }
    }
};