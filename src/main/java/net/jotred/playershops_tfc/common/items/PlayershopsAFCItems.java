package net.jotred.playershops_tfc.common.items;

import net.minecraft.core.registries.Registries;
import net.minecraft.world.item.Item;
import net.minecraftforge.registries.DeferredRegister;
import net.minecraftforge.registries.RegistryObject;

import java.util.Locale;
import java.util.function.Supplier;


public class PlayershopsAFCItems {
    
    public static final DeferredRegister<Item> ITEMS_AFC = DeferredRegister.create(Registries.ITEM, "playershops_tfc");
    
    
    private static RegistryObject<Item> register(String name)
    {
        return register(name, () -> new Item(new Item.Properties()));
    }
    
    private static <T extends Item> RegistryObject<T> register(String name, Supplier<T> item)
    {
        return ITEMS_AFC.register(name.toLowerCase(Locale.ROOT), item);
    }
}
