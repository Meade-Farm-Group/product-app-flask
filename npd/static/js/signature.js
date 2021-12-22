/* jshint esversion: 6 */

// signature pad sign off function
$(document).ready(function() {
    let canvas = document.getElementById("signature-pad");

    canvas.height = 200;
    canvas.width = canvas.offsetWidth;

    let signaturePad = new SignaturePad(canvas);

    $("#clear-sig").click(() => {
        signaturePad.clear();
    });

    $(window).resize(() => {
        canvas.height = 200;
        canvas.width = canvas.offsetWidth;
    });

    $("#submit-sig").click((e) => {
        e.preventDefault(e);

        if (signaturePad.isEmpty()) {
            $("#signature-notification").html("Signature Field Cannot Be Empty!").addClass("text-danger");
        } else {
            $("#signature-data").val(signaturePad.toDataURL());
            $("#signature-form").submit();
        }
    });
});