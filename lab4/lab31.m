%lab4

bindata = csvread('bindigit_trn.csv');
bindatatarget = csvread('targetdigit_trn.csv');
bintestdata = csvread('bindigit_tst.csv');
bintestdatatarget = csvread('targetdigit_tst.csv');
%imagesc(p1)
k = 10;
figure(1)
imshow(reshape(bindata(k,:),28,28));
bindatatarget(k)
autoenc = trainAutoencoder(bindata',100);
Y = predict(autoenc,bindata')';
figure(2)
imshow(reshape(Y(k,:),28,28));

h = plotWeights(autoenc)