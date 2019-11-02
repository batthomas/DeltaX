$(function () {
    $("#id_question").on("change", function () {
        renderPreview($("#id_question"), $("#question-preview"))
    });
    $("#id_approach").on("change", function () {
        renderPreview($("#id_approach"), $("#approach-preview"))
    });
    $("#id_answer").on("change", function () {
        renderPreview($("#id_answer"), $("#answer-preview"))
    });
});

function renderPreview(element, preview) {
    preview.text(element.val());
    renderMathInElement(preview[0], {
        displayMode: true,
        throwOnError: false,
        delimiters: [
            {left: "$$", right: "$$", display: true},
            {left: "\\[", right: "\\]", display: true},
            {left: "$", right: "$", display: false},
            {left: "\\(", right: "\\)", display: false}
        ]
    });

}