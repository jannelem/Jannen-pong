Alla oleva luokkakaavio esittää suunniteltua toimivan ohjelman luokkakaaviota:

```mermaid
classDiagram
GameView "1" -- "1" PongService
PongService "1" -- "1" Pong
Pong "1" -- "2" Paddle
Pong "1" -- "1" Ball
```
