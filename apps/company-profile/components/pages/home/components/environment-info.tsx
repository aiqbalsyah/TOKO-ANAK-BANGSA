export function EnvironmentInfo() {
  return (
    <div className="pt-4 text-center text-sm text-muted-foreground border-t">
      <p>Environment: {process.env.NEXT_PUBLIC_APP_ENV}</p>
      <p>Port: 3002 (Company Profile)</p>
    </div>
  );
}
