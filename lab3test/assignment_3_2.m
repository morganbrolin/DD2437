
clear
close all
clc

A = importdata('pict.dat');
%imagesc(p1)
p_array = [];
P = reshape (A,[1024 11]);

P1 = reshape(P(:,1),[32,32]);
P2 = reshape(P(:,2),[32,32]);
P3 = reshape(P(:,3),[32,32]);
P4 = reshape(P(:,4),[32,32]);
P5 = reshape(P(:,5),[32,32]);
P6 = reshape(P(:,6),[32,32]);
P7 = reshape(P(:,7),[32,32]);
P8 = reshape(P(:,8),[32,32]);
P9 = reshape(P(:,9),[32,32]);
P10 = reshape(P(:,10),[32,32]);
P11 = reshape(P(:,11),[32,32]);


X_train = [reshape(P1,[1,1024]);reshape(P2,[1,1024]);reshape(P3,[1,1024])];
X_test = [reshape(P10,[1,1024])];
W = initialize_weights(X_train);
%X_test  = X_train
ite_max = 3;

[ite,X_out] = weight_update_batch(X_test, ite_max,W);
%W = -1 + (1+1)* rand(1024,1024);
figure(1)

imagesc(reshape((X_out),[32,32]));
%imagesc(P3)
figure(2)
imagesc(P10)