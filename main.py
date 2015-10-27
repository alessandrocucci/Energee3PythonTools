#!/usr/bin/env python
'''
Energee3 Python Tools

Ai colleghi di Energee3:
come suggerisce il nome, si tratta di un insieme di script e tool vari che potrebbero tornare utili nello
sviluppo di codice Python.

PS Pull request ben accette!
'''

__author__ = "Alessandro Cucci"
__package_name__ = "Energee3 Python Tools"
__license__ = "MIT"
__version__ = "0.0.1"
__email__ = "alessandro.cucci@energee.com"
__status__ = "Development"

import argparse


def performance():
    from Scripts import timeit

    timeit.main()


if __name__ == '__main__':
    logo = """

                             .;;;,
                             ;;;;;                          .::
                            `;;;;;                         ;;;;;;
                             ;;;;;                        ;;;;;;;:
                             `;;;                         ;;;;;;;;
                               ;;                        .;;;;;;;;
                               ;;                        ;;;;;;;;;
                               :;                       `;;;;;;;;
                               .;                      `;;;;;;;:
                                ;`                    .;;;;;:`
                                ;:                   :;;;`
                                ;;                  ;;;.
                                ;;                .;;;
       :;;;                     ,;               ;;;.
     `;;;;;;,                   `;`            `;;;
     ;;;;;;;;                    ;:           :;;.
    `;;;;;;;;;                   ;;          ;;;
    .;;;;;;;;;;`                 ;;        ,;;,
     ;;;;;;;;;;;;;.              ;;,      ;;;
     ;;;;;;;;;;;;;;;;:`          :;;    .;;;
     ,;;;;;;;`.,;;;;;;;;;,       ,;;.  ;;;,
      `;;;;,       `:;;;;;;;;`   ,;;;;;;;`
                        .;;;;;;;:;;;;;;;
                            ,;;;;;;;;;;;.
                               ,;;;;;;;;;;;:.       ,.
                                ;;;;;;;,:;;;;;;;. :;;;;
                               ;;;;;;;.     `,:;;;;;;;;;
                             `;;,  :;;:          ;;;;;;;
                            :;;     ;;;           ;;;;;
                           ;;`      `;;           `;;;`
                         .;:         ;;`
                        ;;`           ;;
                   .;;:;;             ;;
                   ;;;;:               ;.
                   ;;;;`               ;;
                   ,;;;                 ;`
                     .                  ;;;
                                        ;;;
                                        ;;;


                       ENERGEE3 PYTHON TOOLS
                            Energee3 srl

    """
    print logo
    parser = argparse.ArgumentParser()

    parser.add_argument('-p', '--performance', action='store_true',
                            help='Execute timeit.py script')

    # TODO: Aggiungere gli altri

    parser.add_argument('--version', action='version', version=' '.join([__package_name__, __version__]))

    results = parser.parse_args()
    if results.performance:
        performance()


