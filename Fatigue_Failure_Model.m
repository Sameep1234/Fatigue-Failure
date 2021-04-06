syms x y r ll %Clear the variables
for n =0:50000:300000 %Loop to iterate and compute the values
f=x^2+y^2; %Lagrange Equation
g=1 - n/(((1100*y + 20900)/(13.5*x + 279)^2)^((1) / (-(1/3)*log((13.5*x +279)/(5*y + 95)))));%Constraint for lagrange
L=f-r*g;%Lagrange Theory Equation
gradL=gradient(L);% Find Gradient and then set it to 0
[xs ys  rs]=solve(gradL==0,[x y r],'Real',true); % Find critical points of L
h=.01;
k=.01;
for i=1:numel(xs)
 %Substitute [x, y] as [xs(i), ys(i)] in eqn f
 fopt=double(subs(f,[x y],[xs(i) ys(i)]));%set double precision
 gc=subs(g,[x y ],[xs(i)+h ys(i)+k+ll]);%h, k is added for extra precision
 l=double(solve(gc==ll));
 [a j]=min(abs(l));%(NOT SURE)Finding minimum distance index
 disp(a);
 l=l(j);%making l to be minimum distance
 fnear=double(subs(f,[x y ],[xs(i)+h ys(i)+k+l]));%Substitute
 [xs(i) ys(i)] %Print it
 
syms x1 y1
g1=1 - n/(((1100*y1 + 20900)/(13.5*x1 + 279)^2)^((1) / (-(1/3)*log((13.5*x1 +279)/(5*y1+ 95)))));
P=diff(g1,y1);
P2=diff(g1,x1);
T=double(subs(P,[x1 y1],[xs(i),ys(i)]));
T2=double(subs(P2,[x1 y1],[xs(i),ys(i)]));

mu = 0;

sigma =sqrt((T^2)*(25)+(T2^2)*(225));
disp(sigma^2);
pd = makedist('Normal','mu',mu,'sigma',sigma);
u= -(ys(i)*T)-(xs(i)*T2);
disp(u);
c=double(cdf(pd,u));
disp(c);
end
end