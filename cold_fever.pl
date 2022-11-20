suggest(D) :- write('Does your nose is runny or stuffy?: '),read(N),write('Is your throat Sore?: '),read(T),write('Do you Sneezing?: '),read(S),write('Are you generally feeling unwell?: '),read(U),write('Do you have a slight body pain?: '),read(P), detect(D,N,T,S,U,P).

detect('Only Cold',N,T,S,U,P):- N=yes,T=yes,S=yes,U=no,P=no,!.
detect('Only Fever',N,T,S,U,P):- N=no,T=no,S=no,U=yes,P=yes,!.
detect('Both Cold and Fever',N,T,S,U,P):- N=yes,T=yes,S=yes,U=yes,P=yes,!.
detect('You are healthy',N,T,S,U,P):- N=no,T=no,S=no,U=no,P=no,!.