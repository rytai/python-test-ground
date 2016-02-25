# coding=utf-8
import random
import sys, pygame

__author__ = 'Kodex'

pygame.init()

ruudun_koko = width, height = 1260, 840

ruutu = pygame.display.set_mode(ruudun_koko)

kello = pygame.time.Clock()


# Pallko luokka
class DasBall():
    nykyinen_pinta = None

    nopeus_x = 4.6
    nopeus_y = 3.3

    pallon_koko = (10, 10)

    pallon_sijainti = (10, 10)

    def __init__(self):
        pass

    # Muutetaan joko x, tai y nopeus päälaelleen.
    def vaihda_suunta(self, suunta):
        if suunta == 'x':
            self.nopeus_x = self.nopeus_x * -1.0
        elif suunta == 'y':
            self.nopeus_y = self.nopeus_y * -1.0

    def paivita(self, ruudun_koko):
        reuna_x, reuna_y = ruudun_koko
        sijainti_x, sijainti_y = self.pallon_sijainti

        # Tarkastetaan, meneekö pallo ruudun yli.
        # Jos menee niin palautetaan se.
        if sijainti_x < 0:
            self.vaihda_suunta('x')
        if sijainti_y < 0:
            self.vaihda_suunta('y')
        if sijainti_x > reuna_x:
            self.vaihda_suunta('x')
        if sijainti_y > reuna_y:
            self.vaihda_suunta('y')

        # Siirretään palloa nopeuden verran.
        sijainti_x += self.nopeus_x
        sijainti_y += self.nopeus_y
        self.pallon_sijainti = sijainti_x, sijainti_y


# Piirtää pallon tietyn värisen pallon, joka passataan palloluokalle
def make_a_ball_surface(vari):
    uusi_pinta = pygame.Surface((20, 20))
    pygame.draw.circle(uusi_pinta, vari, uusi_pinta.get_rect().center, 10)
    return uusi_pinta


# Sisältää kaikki pallot
all_the_ballz = []

oletus_pallo_pinta = make_a_ball_surface((0, 255, 255))

# Nain luodaan uusi pallo
uusin_ballz = DasBall()
all_the_ballz.append(uusin_ballz)

# Näin asetetaan luokkamuuttuja. oletuspallopinta
DasBall.nykyinen_pinta = oletus_pallo_pinta

while 1:
    # Rajoitetaan framerate 40:een.
    kello.tick(40)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
        if event.type == pygame.KEYUP:

            if event.key == pygame.K_SPACE:
                uusin_ballz = DasBall()
                all_the_ballz.append(uusin_ballz)

            if event.key == pygame.K_RETURN:
                random_vari = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                uusi_pinta = make_a_ball_surface(random_vari)
                uusin_ballz.nykyinen_pinta = uusi_pinta

            if event.key == pygame.K_BACKSPACE:
                random_vari = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                uusi_pinta = make_a_ball_surface(random_vari)
                DasBall.nykyinen_pinta = uusi_pinta


                # Tyhjennetään ruutu
    ruutu.fill((0, 0, 0))

    for pallo in all_the_ballz:
        pallo.paivita(ruudun_koko)
        ruutu.blit(pallo.nykyinen_pinta, pallo.pallon_sijainti)

    # Piirretään frame
    pygame.display.flip()
