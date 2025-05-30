// prompt e ParseInt são termos que não foram ensinados na aula mas foram pesquisador por mim em busca de fazer um código mais adequado para a proposta da atividade

let nomeHeroi = prompt("Digite o nome do seu Herói: ");
let numeroXP = parseInt(prompt("Digite a quantidade de seu XP: "));

const niveisXP = [1000, 2000, 5000, 7000, 8000, 9000, 10000];
const niveis = ["Ferro", "Bronze", "Prata", "Ouro", "Platina", "Ascendente", "Imortal", "Radiante"];

const index = niveisXP.findIndex(xp => numeroXP < xp);

const nivel = index !== -1 ? niveis[index] : niveis[niveis.length - 1];

console.log(`O Herói de nome ${nomeHeroi} está no nível de ${nivel}`);
