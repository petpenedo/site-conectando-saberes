function toggleMenu(button) {
    let menu = button.nextElementSibling;

    document.querySelectorAll(".menu-classificacao").forEach(m => {
        if (m !== menu) {
            m.style.display = "none";
        }
    });

    menu.style.display = (menu.style.display === "block") ? "none" : "block";
}

function classificar(questao, classe) {
    let ano = document.getElementById('anoAtual').value;
    let area_conhecimento = document.getElementById('areaAtual').value;

    fetch("/salvar-classificacao/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCSRFToken()
        },
        body: `numero_questao=${questao}&classificacao=${classe}&ano=${ano}&area_conhecimento=${encodeURIComponent(area_conhecimento)}`
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);
    })
    .catch(error => console.error("Erro:", error));
}

function getCSRFToken() {
    return document.querySelector("[name=csrfmiddlewaretoken]").value;
}
