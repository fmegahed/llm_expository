ewma.arl.target <- 500
ewma.arl.optimize <- function(cE) {
  ewma.arl(lam = 0.1, cE = cE, mu = 0, z0 = 0) - ewma.arl.target
}

cE <- uniroot(ewma.arl.optimize, interval = c(0, 100))$root
cE
