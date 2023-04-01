Dropzone.options.rrrDropzone = { // camel-ized version of the 'id'
    paramName: "file", // The name that will be used to transfer the file
    addRemoveLinks: true, // Allows to un-attach or remove uploaded content
    // url: "http://www.csce.uark.edu/~yrdubasi/cgi-bin/RRR.cgi", // Where images get uploaded
    uploadMultiple: false,
    maxFiles: 1,
    accept: function(file, done) {
        if (file.name == "potato.txt") {
            done("DENIED: I see you... always");
        }
        else { done(); }
    },
    init: function() {
        this.on("addedfile", function() {
            if (this.files[1]!=null){
                this.removeFile(this.files[0]);
            }
        });
    }
};