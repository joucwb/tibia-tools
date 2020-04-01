# Tutorial de Configuração

## 1. Instalando KUMAS e os requerimentos

1. Na página do [KUMAS](https://github.com/SamuelBFG/tibia-tools), baixe a pasta como ZIP, como indica a imagem abaixo:

![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/install.png?raw=true "Download KUMAS")

2. Unzipe o *download* feito e navegue até a pasta Trainer, clique na barra de diretório (caminho), onde está em vermelho na imagem abaixo:

![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/install0_0.png?raw=true "Find path")

3. Copie o diretório como indica a imagem:

![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/install0_1.png?raw=true "Copy path")

4. Feito isso, abra o seu cmd (tecle Windows+S ou Windows+R e digite cmd)<br/>
*Obs: Existem [várias maneiras](https://www.techtudo.com.br/listas/noticia/2016/05/mais-de-dez-maneiras-de-abrir-o-prompt-de-comando-no-windows-10.html) de acessar seu cmd.*

![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/config0_0.png?raw=true "Open cmd")

5. Após abrir seu *prompt de comando* (cmd), navegue até a o diretório que você acabou de copiar, para isso tecle cd + diretório. No 
exemplo do tutorial, ficaria:
```shell
cd C:\Users\Samuel Gomes\Desktop\tibia-tools-master\Trainer
```
![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/install1_0.png?raw=true "Cd cmd")

6. Estando no diretório correto (Trainer), instale os pacotes auxiliares necessários teclando:
```shell
pip install -r requirements.txt
```
![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/install1_1.png?raw=true "Install requirements.txt")

7. Aguarde o tempo necessário para o *download* dos pacotes, e finalmente podemos abrir o KUMAS Trainer, para isso, tecle:
```shell
python kumas.py
```
![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/install2_0.png?raw=true "deploying KUMAS")

8. A tela inicial do app vai abrir, como indica a imagem abaixo:


## 2. Configurando seu KUMAS pela primeira vez:


![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/kumas0.png?raw=true "KUMAS")

1. Entradas:

- **Character Name:** Coloque o nick do seu personagem.
- **Food:** Hotkey da food.
- **Ring:** Hotkey do ring.
- **Soft:** Hotkey da soft boots.
- **Rune:** Hotkey para runar.
- **Screenshot:** Hotkey para tirar *Screenshots*.
- **Botão *Browse:*** Coloque o diretório das screenshots do Tibia.
- **Botão *Save Configs:*** Salva as configurações atuais.
- **Cycle Time:** Tempo de cada ciclo (a cada tempo de ciclo será runado o numero de runas setado) em minutos.
- **Runes per cycle:** Runas por ciclo. Quantas runas serão runadas a cada ciclo.

2. Antes de iniciar o treino, precisamos configurar nosso client do Tibia para deixar o ambiente preparado:

- Primeiramente precisamos configurar uma *hotkey* para tirar screenshots dentro das *options* (tecla de atalho: crtl+k) do Tibia client, 
no exemplo deste tutorial, foi setado a tecla f12, como mostra a imagem abaixo:

![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/config1_0.png?raw=true "Screenshot hotkey")

É recomendado que você escolha a mesma *hotkey* para ambos *Chat On* e *Chat Off*

- Após isso, vá em ***Interface*** e escolha a opção *Corners* para Colourise Loot Value:

![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/config2_0.png?raw=true "Corners")

- Depois vá em ***Interface >> HUD*** e deixe habilitado a opção *Show Status Bar*.

![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/config3_0.png?raw=true "Status Bar")

- Por fim, vá em ***Misc. >> Screenshots*** e desmarque a opção *Only Capture Game Window*. É também nessa aba que você pode clicar no botão
*Open Screenshot Folder* para saber onde fica o diretório de screenshots do Tibia no seu computador.

![alt text](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/imgs/config4_0.png?raw=true "Status Bar")

3. *Pronto!* Seu KUMAS ja está pronto para ser utilizado, não esqueça que **SUA MANA PRECISA ESTAR
CHEIA** antes de clicar no botão de treinar! Clique [aqui](https://github.com/SamuelBFG/tibia-tools/blob/master/Trainer/tutorial/tut_2.md) para aprender como rodar o programa.

