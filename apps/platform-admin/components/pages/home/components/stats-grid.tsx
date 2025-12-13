interface StatItemProps {
  value: number;
  label: string;
}

function StatItem({ value, label }: StatItemProps) {
  return (
    <div className="text-center">
      <p className="text-2xl font-bold">{value}</p>
      <p className="text-xs text-muted-foreground">{label}</p>
    </div>
  );
}

export function StatsGrid() {
  const stats = [
    { value: 0, label: 'Tenants' },
    { value: 0, label: 'Products' },
    { value: 0, label: 'Orders' },
  ];

  return (
    <div className="grid grid-cols-3 gap-2 pt-4 border-t">
      {stats.map((stat) => (
        <StatItem key={stat.label} {...stat} />
      ))}
    </div>
  );
}
