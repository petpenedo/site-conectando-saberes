function toggleMenu(button) {
    let menu = button.nextElementSibling;

    // Fecha outros menus antes de abrir o atual
    document.querySelectorAll(".menu-classificacao").forEach(m => {
        if (m !== menu) {
            m.style.display = "none";
        }
    });

    menu.style.display = (menu.style.display === "block") ? "none" : "block";
}

function classificar(questao, classe) {
    fetch("/salvar-classificacao/", {
        method: "POST",
        headers: {
            "Content-Type": "application/x-www-form-urlencoded",
            "X-CSRFToken": getCSRFToken()
        },
        body: `numero_questao=${questao}&classificacao=${classe}`
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // Exibe mensagem de sucesso ou erro
    })
    .catch(error => console.error("Erro:", error));
}

// Função para obter o token CSRF do Django
function getCSRFToken() {
    return document.querySelector("[name=csrfmiddlewaretoken]").value;
}
