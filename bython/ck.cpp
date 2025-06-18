#include <stdio.h>

#include <string.h>
#include <conio.h>

#define Inf 10000
#define MAX 10

typedef int MATRIX[MAX][MAX];

MATRIX a[MAX*MAX],t[MAX*MAX];

int n,na, fmin;
int cost[MAX*MAX],bound[MAX*MAX], d[MAX*MAX], ht[MAX];
// a: day ma tran lay ra de tim hanh trinh, khoi dau la hanh trinh goc
// t: day hanh trinh, t={0} ban dau
// na: so hanh trinh luu vao ngan xep
// bound: can tren cua cac hanh trinh, bound[0]=0
// cost: do dai cac hanh trinh,cost[0]=0
// d: danh dau hanh trinh da duyet

FILE *fi,*fo;

int Hamilton(int);
void xuatht(MATRIX),inmatran(MATRIX,MATRIX), vedt(MATRIX);

int main()
{
  char fn[40],fin[40],fon[40], s[40],ss[40];
  int i,j,k,bmin,done,nc,baitoan=0;

  //system("COLOR F0");
  printf("File(*.INP): "); gets(fn); strupr(fn);
  strcpy(fin,fn); strcpy(fon,fn);
  strcat(fin,".INP"); strcat(fon,".OUT");
  fi=fopen(fin,"rt");  fo=stdout; //fo=fopen(fon,"wt"); 
  fprintf(fo,"BAI TOAN  TSP\n\n");
  fscanf(fi,"%d",&n);
  for (i=0; i<n; i++){
      for (j=0; j<n; j++) fscanf(fi,"%d",&a[0][i][j]);
      fscanf(fi,"%*c");//doc sang dong
  }

  for (i=0; i<n; i++){
      for (j=0; j<n; j++)
		if (a[0][i][j]<Inf){
	  		printf("%-5d",a[0][i][j]);
	  		fprintf(fo,"%-5d",a[0][i][j]);
		}
		else{
	  		printf("%-5c",'?');  fprintf(fo,"%-5c",'?');
		}
      printf("\n"); fprintf(fo,"\n");
  }
  getchar();

  for (i=0; i<n; i++)
      for (j=0; j<n; j++)
		if (!a[0][i][j]) a[0][i][j]=Inf;
    // xoa khuyen
  for (i=0; i<n; i++) a[0][i][i]=Inf;
    // chu trinh ban dau rong
  na=0;
  for (i=0; i<n; i++)
      for (j=0; j<n; j++)
		 t[0][i][j]=0;
  cost[0]=0;

  na=1;
  printf("\nXet nhanh goc\n\n"); getch();
  fprintf(fo,"\nXet nhanh goc\n\n");
  fmin=Inf; d[0]=1; cost[0]=Hamilton(0); fmin=cost[0];
  printf("Do dai hanh trinh ban dau: ");
  fprintf(fo,"Do dai hanh trinh ban dau: ");
  if (fmin<Inf) printf("%d\n",fmin); else printf("?\n");
  if (fmin<Inf) fprintf(fo,"%d\n",fmin); else fprintf(fo,"?\n");

  getch();
  done=0;
  while (!done){
      bmin=fmin; i=0;
      for (j=1;j<na;j++)
		if (!d[j] && bound[j]<=bmin && bound[j]<Inf){ 
			i=j; bmin=bound[j];
		}
      if (i==0) done=1;
      else{
		printf("\nXet nhanh co can duoi: \%d\n",bound[i]);
		getch();
		fprintf(fo,"\nXet nhanh co can duoi: \%d\n",bound[i]);
		d[i]=1;
		cost[i]=Hamilton(i);
		if (cost[i]<fmin) fmin=cost[i];
      }
  }
  if (fmin>=Inf) {
      printf("NO HAMILTON...");
      fprintf(fo,"NO HAMILTON...");
      getch();
  }
  else{
  	for (nc=0,i=0;i<na;i++)
	if (d[i] && cost[i]==fmin) nc++;
    printf("Co %d hanh trinh toi uu ",nc);
    fprintf(fo,"Co %d hanh trinh toi uu ",nc);
    printf("voi do dai ngan nhat: %d\n",fmin);
    fprintf(fo,"voi do dai ngan nhat: %d\n",fmin);
    for (nc=0,i=0;i<na;i++)
		if (d[i] && cost[i]==fmin) {
	  		nc++;
	  		printf("Hanh trinh %d: ",nc);
	  		fprintf(fo,"Hanh trinh %d: ",nc);
	  		xuatht(t[i]);
		}
  }
  printf("\n"); fprintf(fo,"\n");
  fclose(fi); fclose(fo);
}

int Hamilton(int ia)
{
  MATRIX x, y;
  int i,j,k,col,row,r[MAX],c[MAX],minr[MAX],minc[MAX],sum,
      loop,done,tr,tc,fc;

      // r, c: danh dau hang/cot da xoa
      // fc: cuoc phi cuoi cung cua a
      // sum la tong rut gon

  // chep a sang x va t sang y de tinh

  for (i=0; i<n; i++)
    for (j=0; j<n; j++) {
      x[i][j]=a[ia][i][j];
      y[i][j]=t[ia][i][j];
    }

  //xoa cac hang i / cot j voi canh (i,j) da nap vao hanh trinh
  for (i=0; i<n; i++) {r[i]=1; c[i]=1;}

  loop=n;
  for (i=0; i<n; i++)
    for (j=0; j<n; j++)
      if (y[i][j]) {r[i]=0; c[j]=0; loop--;}

  inmatran(x,y);
  printf("Cac canh da nap vao:\n");
  fprintf(fo,"Cac canh da nap vao:\n");
  for (i=0; i<n; i++)
    for (j=0; j<n; j++)
      if (y[i][j]){
	printf("(%d,%d),",i+1,j+1);
	fprintf(fo,"(%d,%d),",i+1,j+1);
      }
  printf("\n");
  fprintf(fo,"\n");
  fc=cost[ia];

  while (loop>2 && fc<=fmin){
    printf("vong lap (%d)\n",n-loop+1);
    fprintf(fo,"vong lap (%d)\n",n-loop+1);
    //rut gon dong
    sum=0;
    for (i=0; i<n; i++) if (r[i]){
      minr[i]=Inf;
      for (j=0; j<n; j++)
	if (c[j] && x[i][j]<minr[i]) minr[i]=x[i][j];
      for (j=0; j<n; j++) if (c[j])
	if (x[i][j]<Inf) x[i][j]-=minr[i];
      sum+=minr[i];
    }

    //rut gon cot
    for (j=0; j<n; j++) if (c[j]){
      minc[j]=Inf;
      for (i=0; i<n; i++)
	if (r[i] && x[i][j]<minc[j]) minc[j]=x[i][j];
      for (i=0; i<n; i++) if (r[i])
	if (x[i][j]<Inf) x[i][j]-=minc[j];
      sum+=minc[j];
    }
   fc+=sum;

    printf("Rut gon dong: ");
    for (i=0; i<n; i++)
      if (r[i])
	if (minr[i]<Inf) printf("%-5d",minr[i]); else printf("%-5c",'?');
      else printf("%-5c",'.');
    printf("\n");
    fprintf(fo,"Rut gon dong: ");
    for (i=0; i<n; i++)
      if (r[i])
	if (minr[i]<Inf) fprintf(fo,"%-5d",minr[i]); else fprintf(fo,"%-5c",'?');
      else fprintf(fo,"%-5c",'.');
    fprintf(fo,"\n");

    printf("Rut gon cot: ");
    for (j=0; j<n; j++)
      if (c[j])
	if (minc[j]<Inf) printf("%-5d",minc[j]); else printf("%-5c",'?');
      else printf("%-5c",'.');
    printf("\n");
    fprintf(fo,"Rut gon cot: ");
    for (j=0; j<n; j++)
      if (c[j])
	if (minc[j]<Inf) fprintf(fo,"%-5d",minc[j]); else fprintf(fo,"%-5c",'?');
      else fprintf(fo,"%-5c",'.');
    fprintf(fo,"\n");

    printf("Tong rut gon: ");
    if (sum<Inf) printf("%d\n",sum); else printf("?\n");
    fprintf(fo,"Tong rut gon: ");
    if (sum<Inf) fprintf(fo,"%d\n",sum); else fprintf(fo,"?\n");

    //in lai ma tran sau khi rut gon
    inmatran(x,y);

    if (fc>=Inf) return Inf;

    //tim canh (i,j) nap vao hanh trinh
    // tinh can tren cua cac nhanh khac
    // tim canh (i,j) co tong chenh lech sum lon nhat
    sum=-Inf;
    for (i=0; i<n; i++)
      for (j=0; j<n; j++)
	if (r[i] && c[j] && x[i][j]==0){
	  tr=Inf;
	  for (k=0; k<n; k++)
	    if (k!=j &&  c[k] && x[i][k]<tr) tr=x[i][k];
	  tc=Inf;
	  for (k=0; k<n; k++)
	    if (k!=i && r[k] && x[k][j]<tc) tc=x[k][j];
	  if (tr+tc>sum){
	    sum=tr+tc;
	    row=i;
	    col=j;
	  }
	}

    // luu nhanh khong chua canh (i,j)
    for (i=0; i<n; i++)
      for (j=0; j<n; j++) {
	a[na][i][j]=x[i][j];
	t[na][i][j]=y[i][j];
      }
    a[na][row][col]=Inf; cost[na]=fc; bound[na]=fc+sum;
    na++;
    // nap canh (i,j) vao hanh trinh, xoa hang i cot j
    printf("Nap canh(%d,%d)\n",row+1,col+1);
    fprintf(fo,"Nap canh(%d,%d)\n",row+1,col+1);
    printf("Do dai hien thoi cua hanh trinh: ",fc);
    fprintf(fo,"Do dai hien thoi cua hanh trinh: ",fc);
    if (fc<Inf) printf("%d\n",fc); else printf("?\n");
    if (fc<Inf) fprintf(fo,"%d\n",fc); else fprintf(fo,"?\n");
    printf("Nhanh hanh trinh chua ");
    for (i=0; i<n; i++)
      for (j=0; j<n; j++)
	if (y[i][j]) printf("(%d,%d),",i+1,j+1);
    printf("khong chua (%d,%d) co can duoi: ",row+1,col+1);

    fprintf(fo,"Nhanh hanh trinh chua ");
    for (i=0; i<n; i++)
      for (j=0; j<n; j++)
	if (y[i][j]) fprintf(fo,"(%d,%d),",i+1,j+1);
    fprintf(fo,"khong chua (%d,%d) co can duoi: ",row+1,col+1);
    if (fc+sum<Inf) printf("%d\n",fc+sum); else printf("?\n");
    if (fc+sum<Inf) fprintf(fo,"%d\n",fc+sum); else fprintf(fo,"?\n");

    // nap canh (i,j) vao hanh trinh, xoa hang i cot j
    y[row][col]=1; r[row]=0; c[col]=0;

    //ngan cam hanh trinh con khi nap canh (i,j)
    // truong hop s->...->(i->j)->...->t loai canh (t,s)
    j=row; done=0;
    while (!done){
      k=0; while (k<n && !y[k][j]) k++;
      if (k<n) j=k; else done=1;
    }
    i=col; done=0;
    while (!done){
      k=0; while (k<n && !y[i][k]) k++;
      if (k<n) i=k; else done=1;
    }
    x[i][j]=Inf;
    printf("Ngan cam hanh trinh con, can dat c(%d,%d)=?\n",i+1,j+1);
    fprintf(fo,"Ngan cam hanh trinh con, can dat c(%d,%d)=?\n",i+1,j+1);

    //in lai ma tran sau khi giam cap
    inmatran(x,y);
    loop--;
  }
  //rut gon dong
    sum=0;
    for (i=0; i<n; i++) if (r[i]){
      minr[i]=Inf;
      for (j=0; j<n; j++)
	if (c[j] && x[i][j]<minr[i]) minr[i]=x[i][j];
      for (j=0; j<n; j++) if (c[j])
	if (x[i][j]<Inf) x[i][j]-=minr[i];
      sum+=minr[i];
    }

    //rut gon cot
    for (j=0; j<n; j++) if (c[j]){
      minc[j]=Inf;
      for (i=0; i<n; i++)
	if (r[i] && x[i][j]<minc[j]) minc[j]=x[i][j];
      for (i=0; i<n; i++) if (r[i])
	if (x[i][j]<Inf) x[i][j]-=minc[j];
      sum+=minc[j];
    }
   if (fc<Inf) fc+=sum;

    printf("Rut gon dong: ");
    for (i=0; i<n; i++)
      if (r[i])
	if (minr[i]<Inf) printf("%-5d",minr[i]); else printf("%-5c",'?');
      else printf("%-5c",'.');
    printf("\n");
    fprintf(fo,"Rut gon dong: ");
    for (i=0; i<n; i++)
      if (r[i])
	if (minr[i]<Inf) fprintf(fo,"%-5d",minr[i]); else fprintf(fo,"%-5c",'?');
      else fprintf(fo,"%-5c",'.');
    fprintf(fo,"\n");

    printf("Rut gon cot: ");
    for (j=0; j<n; j++)
      if (c[j])
	if (minc[j]<Inf) printf("%-5d",minc[j]); else printf("%-5c",'?');
      else printf("%-5c",'.');
    printf("\n");
    fprintf(fo,"Rut gon cot: ");
    for (j=0; j<n; j++)
      if (c[j])
	if (minc[j]<Inf) fprintf(fo,"%-5d",minc[j]); else fprintf(fo,"%-5c",'?');
      else fprintf(fo,"%-5c",'.');
    fprintf(fo,"\n");

    printf("Tong rut gon: ");
    if (sum<Inf) printf("%d\n",sum); else printf("?\n");
    fprintf(fo,"Tong rut gon: ");
    if (sum<Inf) fprintf(fo,"%d\n",sum); else fprintf(fo,"?\n");

    //in lai ma tran sau khi rut gon
    inmatran(x,y);

    if (fc>=Inf) return Inf;

  //nap hai canh cuoi cung
  if (fc<=fmin)
    for (i=0; i<n; i++)
      for (j=0; j<n; j++)
	if (r[i] && c[j] && !x[i][j]){
	  if (fc<Inf) fc+=x[i][j]; y[i][j]=1;
	  printf("nap canh (%d,%d)\n",i+1,j+1);
	  fprintf(fo,"nap canh (%d,%d)\n",i+1,j+1);
	}
  printf("Do dai cua hanh trinh tim duoc: ",fc);
  if (fc<Inf) printf("%d\n",fc); else printf("?\n");
  fprintf(fo,"Do dai cua hanh trinh tim duoc: ",fc);
  if (fc<Inf) fprintf(fo,"%d\n",fc); else fprintf(fo,"?\n");

  //luu lai hanh trinh tim duoc
  for (i=0; i<n; i++)
    for (j=0; j<n; j++) t[ia][i][j]=y[i][j];

  return fc;
}

void xuatht(MATRIX y)
{
  int i,j,k;

  i=0; j=0; ht[j]=i;
  do {
    k=0; while (k<n && !y[i][k]) k++;
    i=k; ht[++j]=i;
  } while (i!=0);

  printf("%d ",ht[0]+1);
  fprintf(fo,"%d ",ht[0]+1);

  for (i=1; i<=n; i++) {
    printf("---> %d ",ht[i]+1);
    fprintf(fo,"---> %d ",ht[i]+1);
  }
  printf("\n");
  fprintf(fo,"\n");
  getch();
}

void inmatran(MATRIX x, MATRIX y)
{
  int i,j,r[MAX], c[MAX];

  for (i=0; i<n; i++) {r[i]=1; c[i]=1;}
  for (i=0; i<n; i++)
    for (j=0; j<n; j++) if (y[i][j]) {r[i]=0; c[j]=0;}

  for (i=0; i<n; i++) {
    for (j=0; j<n; j++)
      if (r[i] && c[j])
	if (x[i][j]<Inf) printf("%-5d",x[i][j]); else printf("%-5c",'?');
      else printf("%-5c",'.');
      printf("\n");
  }
  for (i=0; i<n; i++) {
    for (j=0; j<n; j++)
      if (r[i] && c[j])
	if (x[i][j]<Inf) fprintf(fo,"%-5d",x[i][j]); else fprintf(fo,"%-5c",'?');
      else fprintf(fo,"%-5c",'.');
      fprintf(fo,"\n");
  }

  getch();
}