function [WIN ] = som_circular_neighbour(data, no_of_epochs, size_of_neighbourhood, learning_rate)
% SOM algoritm for Topological Ordering of ANimal Species
% Detailed explanation goes here

X = data;
X_size = size(data);
N_row = X_size(1);
N_col = X_size(2);
etha = learning_rate;
N_nodes = N_row;
N_epochs = no_of_epochs;
N_neigh = size_of_neighbourhood;
ite_ind = 1;

% Weight matrix initilization
W = rand (N_nodes, N_col);

while ite_ind <= N_epochs
    for j = 1: 1: N_row
        d = zeros(N_nodes, 1);
        for k = 1: 1: N_nodes
            x = X(j,:);
            w = W(k,:);
            d(k) = sqrt((x - w)*(x - w)');
        end
        win = find(d(:) == min(d(:)));
        neigh_nodes = win: 1 : (win + N_neigh);
        for l = 1 : 1 : length(neigh_nodes)
            if neigh_nodes(l)> N_row
                neigh_nodes(l) = neigh_nodes(l) - N_row;
            end
        end
        
        for m = 1: 1: N_nodes
            if ismember(m, neigh_nodes) == 1
                W(m,:) = W(m,:) + etha*(X(j,:) - W(m,:));
            end
        end
    end
    ite_ind = ite_ind+1;
end

WIN = zeros(N_row,1);
% Printing out the results
for j = 1: 1: N_row
    d_f = zeros(N_nodes,1);
    for k = 1: 1: N_nodes
        x = X(j,:);
        w = W(k,:);
        d_f(k) = sqrt((x -w)*(x - w)');
    end
    win_f = find(d_f(:) == min(d_f(:)));
    if length(win_f)> 1
        WIN(j) = win_f(1);
    else
        WIN(j) = win_f(:);
    end
end



