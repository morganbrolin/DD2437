function [ W ] = weight_calc_sparse_wrong( patterns, normalize, correct_diag,activity)

[P,N] = size(patterns);

if nargin < 3
    correct_diag = true;
end

if nargin <2
    normalize = false;
end



patterns = patterns - activity;
W = patterns'*patterns;
Wsum =sum(sum(W));

if normalize
    W = W./N;
end

if correct_diag
        N = size(W,1);
    W(1:N+1:end)=0;
end

end