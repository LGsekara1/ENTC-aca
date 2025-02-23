A=1;
t = -0.5:0.01:0.5;
p = -2:0.01:2;

%Since t and p are independent a meshgrid is needed
[T,P] = meshgrid(t,p);

% When Y>T gives 1
% E = (1-P).*(normcdf(T-A)) + (P).*(1-normcdf(T+A));
% P(E) is min for T slightly (+) of mean 

% When Y<=T gives 1
E = (P).*(normcdf(T-A)) + (1-P).*(1-normcdf(T+A));
% P(E) is min for T slightly (-) of mean

figure;
surf(T, P, E);
xlabel("\tau")
ylabel("p")
zlabel("Probability of error, P(E)")
title("Probability of Error Distribution")
shading interp; % Smooth the surface
colorbar; % Add a color legend